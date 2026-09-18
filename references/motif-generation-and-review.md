# Motif generation and review

Use this reference for stage 1.

## Default route

Run:

```bash
{python} "{skillDir}/scripts/generate_candidates.py" --output-dir music-workbench/motif-candidates
```

Defaults:

- 12 candidates;
- about 8–12 seconds each;
- the same simple synthesized sound;
- similar loudness and duration;
- numbered files such as `candidate-01.wav`;
- a local listening page that opens after generation.

The script uses only the Python standard library. Use `--seed NUMBER` when the same batch must be reproduced. Use `--no-open` only for headless execution or automated validation; during the actual workflow, open the page for the user.

If the requested output directory already contains files, the generator creates a timestamped `batch-...` subdirectory. It never overwrites an earlier batch.

## Page structure

`assets/review-page.html` is the fixed page framework. Candidate content stays outside it:

- `tracks.js` contains the numbered audio list;
- WAV files contain the actual candidates;
- `manifest.json` records the batch and file metadata.

`scripts/build_review_page.py` can rebuild the same page from an existing directory of WAV files:

```bash
{python} "{skillDir}/scripts/build_review_page.py" MUSIC_DIRECTORY --open
```

Do not hand-edit the page for each project. Change the WAV files or generated track list.

## Review behavior

The page must let the user:

- play candidates one at a time;
- play all candidates in order;
- stop playback;
- loop one candidate;
- download the numbered WAV files.

Ask the user to choose by number. They may simply say that one feels more suitable. Do not invent technical explanations for their choice.

## Stage completion

Stage 1 is complete only when:

- every numbered WAV exists;
- `review.html`, `tracks.js`, and `manifest.json` exist;
- the listening page has been opened;
- the user has selected one candidate;
- the selected WAV has been copied to `music-workbench/selected-motif/`.
