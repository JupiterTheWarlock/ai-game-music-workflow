#!/usr/bin/env python3
"""Generate short, consistently voiced motif candidates using only Python."""

from __future__ import annotations

import argparse
import math
import random
import struct
import wave
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from build_review_page import build_review_page


SAMPLE_RATE = 22_050
ROOT_MIDI = 50  # D3
SCALE = (0, 3, 5, 7, 10, 12, 15, 17)  # minor pentatonic across two octaves


def midi_frequency(note: int) -> float:
    return 440.0 * (2.0 ** ((note - 69) / 12.0))


def choose_phrase(rng: random.Random) -> List[Optional[int]]:
    """Create a memorable phrase with repetition, variation, and short rests."""
    start = rng.randrange(0, 4)
    steps = [start]
    for _ in range(3):
        steps.append(max(0, min(len(SCALE) - 1, steps[-1] + rng.choice((-2, -1, 1, 1, 2)))))
    phrase: List[Optional[int]] = steps + [None, steps[1], steps[2], steps[0]]
    variation = phrase.copy()
    change_index = rng.choice((1, 2, 5, 6, 7))
    if variation[change_index] is not None:
        variation[change_index] = max(
            0,
            min(len(SCALE) - 1, int(variation[change_index]) + rng.choice((-1, 1))),
        )
    return phrase + variation


def envelope(position: int, total: int) -> float:
    attack = max(1, int(total * 0.06))
    release = max(1, int(total * 0.18))
    if position < attack:
        return position / attack
    if position >= total - release:
        return max(0.0, (total - position - 1) / release)
    return 1.0


def render_candidate(path: Path, rng: random.Random) -> float:
    tempo = rng.randint(84, 112)
    unit_seconds = 60.0 / tempo
    phrase = choose_phrase(rng)
    # ``choose_phrase`` already returns the phrase followed by a small variation.
    repeats = 1
    lead_in_units = 0.5
    tail_units = 1.0
    total_seconds = lead_in_units * unit_seconds + len(phrase) * repeats * unit_seconds + tail_units * unit_seconds
    # Keep the promised review length while retaining the same rhythmic structure.
    if total_seconds < 8.0:
        unit_seconds *= 8.0 / total_seconds
    elif total_seconds > 12.0:
        unit_seconds *= 12.0 / total_seconds

    pcm = bytearray()

    def write_silence(seconds: float) -> None:
        pcm.extend(b"\x00\x00" * int(seconds * SAMPLE_RATE))

    def write_note(midi: int, seconds: float) -> None:
        sample_count = int(seconds * SAMPLE_RATE)
        frequency = midi_frequency(midi)
        phase_offset = rng.random() * math.tau
        for sample_index in range(sample_count):
            time = sample_index / SAMPLE_RATE
            tone = math.sin(math.tau * frequency * time + phase_offset)
            tone += 0.24 * math.sin(math.tau * frequency * 2.0 * time + phase_offset)
            tone += 0.08 * math.sin(math.tau * frequency * 3.0 * time + phase_offset)
            value = int(11_000 * envelope(sample_index, sample_count) * tone / 1.32)
            pcm.extend(struct.pack("<h", max(-32768, min(32767, value))))

    write_silence(lead_in_units * unit_seconds)
    for _ in range(repeats):
        for scale_index in phrase:
            if scale_index is None:
                write_silence(unit_seconds)
            else:
                # A small gap keeps notes readable without changing the shared instrument.
                write_note(ROOT_MIDI + SCALE[scale_index], unit_seconds * 0.84)
                write_silence(unit_seconds * 0.16)
    write_silence(tail_units * unit_seconds)

    with wave.open(str(path), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(SAMPLE_RATE)
        output.writeframes(pcm)
    return len(pcm) / 2 / SAMPLE_RATE


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成短旋律候选 WAV 和本地试听页。")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("music-workbench/motif-candidates"),
        help="候选 WAV 与试听页的输出目录",
    )
    parser.add_argument("--count", type=int, default=12, help="候选数量，默认 12")
    parser.add_argument("--seed", type=int, help="固定随机种子，便于再次生成相同结果")
    parser.add_argument("--no-open", action="store_true", help="生成后不自动打开试听页")
    return parser.parse_args()


def choose_batch_directory(requested_dir: Path) -> Path:
    requested_dir = requested_dir.resolve()
    requested_dir.mkdir(parents=True, exist_ok=True)
    if not any(requested_dir.iterdir()):
        return requested_dir

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate = requested_dir / f"batch-{timestamp}"
    suffix = 2
    while candidate.exists():
        candidate = requested_dir / f"batch-{timestamp}-{suffix:02d}"
        suffix += 1
    candidate.mkdir(parents=True)
    print(f"输出目录已有内容，本批候选将保存到：{candidate}")
    return candidate


def main() -> None:
    args = parse_args()
    if args.count < 1 or args.count > 99:
        raise SystemExit("--count 必须在 1 到 99 之间。")

    output_dir = choose_batch_directory(args.output_dir)
    rng = random.Random(args.seed)
    for index in range(1, args.count + 1):
        path = output_dir / f"candidate-{index:02d}.wav"
        duration = render_candidate(path, rng)
        print(f"已生成 {path.name}（{duration:.1f} 秒）")

    review_path = build_review_page(output_dir, open_page=not args.no_open)
    print(f"已生成试听页：{review_path}")


if __name__ == "__main__":
    main()
