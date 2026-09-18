#!/usr/bin/env python3
"""Build a reusable local review page for WAV files."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import wave
import webbrowser
from pathlib import Path
from typing import Optional
from urllib.parse import quote


SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TEMPLATE = SKILL_ROOT / "assets" / "review-page.html"


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as audio:
        frame_rate = audio.getframerate()
        return audio.getnframes() / frame_rate if frame_rate else 0.0


def build_review_page(
    audio_dir: Path,
    output_dir: Optional[Path] = None,
    template: Path = DEFAULT_TEMPLATE,
    open_page: bool = False,
) -> Path:
    audio_dir = audio_dir.resolve()
    output_dir = (output_dir or audio_dir).resolve()
    template = template.resolve()

    if not audio_dir.is_dir():
        raise FileNotFoundError(f"音频目录不存在：{audio_dir}")
    if not template.is_file():
        raise FileNotFoundError(f"试听页模板不存在：{template}")

    wav_files = sorted(
        (path for path in audio_dir.iterdir() if path.is_file() and path.suffix.lower() == ".wav"),
        key=lambda path: path.name.casefold(),
    )
    if not wav_files:
        raise ValueError(f"目录中没有 WAV 文件：{audio_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)
    tracks = []
    for index, wav_path in enumerate(wav_files, start=1):
        try:
            duration = round(wav_duration(wav_path), 3)
        except (wave.Error, EOFError) as exc:
            raise ValueError(f"无法读取 WAV 文件：{wav_path.name}") from exc
        if audio_dir == output_dir:
            page_audio_path = wav_path
            relative_path = Path(wav_path.name)
        else:
            copied_audio_dir = output_dir / "audio"
            copied_audio_dir.mkdir(parents=True, exist_ok=True)
            page_audio_path = copied_audio_dir / wav_path.name
            shutil.copy2(wav_path, page_audio_path)
            relative_path = Path("audio") / wav_path.name
        src = quote(relative_path.as_posix())
        tracks.append(
            {
                "id": f"{index:02d}",
                "filename": wav_path.name,
                "src": src,
                "duration": duration,
            }
        )

    manifest = {
        "format_version": 1,
        "track_count": len(tracks),
        "tracks": tracks,
    }
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    tracks_json = json.dumps(tracks, ensure_ascii=False, indent=2).replace("</", "<\\/")
    (output_dir / "tracks.js").write_text(
        f"window.REVIEW_TRACKS = {tracks_json};\n", encoding="utf-8"
    )

    review_path = output_dir / "review.html"
    shutil.copyfile(template, review_path)
    if open_page:
        opened = webbrowser.open(review_path.as_uri())
        if not opened:
            print(f"未能自动打开浏览器，请手动打开：{review_path}", file=sys.stderr)
    return review_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="为一个 WAV 目录生成本地试听页。")
    parser.add_argument("audio_dir", type=Path, help="包含 WAV 文件的目录")
    parser.add_argument("--output-dir", type=Path, help="页面输出目录；默认与音频目录相同")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE, help="试听页 HTML 模板")
    parser.add_argument("--open", action="store_true", dest="open_page", help="生成后打开试听页")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    review_path = build_review_page(
        args.audio_dir,
        output_dir=args.output_dir,
        template=args.template,
        open_page=args.open_page,
    )
    print(f"已生成试听页：{review_path}")


if __name__ == "__main__":
    main()
