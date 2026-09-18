---
name: ai-game-music-workflow
description: Generate short numbered motif candidates with an offline listening page, turn plain-language scene needs into prompts, then use Suno Cover and focused prompt revisions to create consistent game music.
---

# AI game music workflow

Create a recognizable musical identity in three stages:

1. Generate short motif candidates and let the user choose one on a listening page.
2. Turn the user's scene and style needs into prompts.
3. Use Suno Cover to arrange the selected motif, then revise one problem at a time.

`{skillDir}` means the directory containing this `SKILL.md`. Resolve bundled scripts and assets from that directory rather than from the user's current working directory. `{python}` means an available Python 3.8 or newer command such as `python`, `python3`, or `py -3`.

Do not imitate the melody or recording of a named game. A named reference may explain the desired level of recognizability, but the generated melody must be original.

## Keep the workflow beginner-friendly

- Ask in everyday language. Do not require music theory terms.
- Treat the user's selection and listening reaction as preference. Do not invent reasons they did not give.
- At each stage, show the visible result before moving on.
- Preserve previous files and generations instead of overwriting them.
- If the user already provides a short motif WAV, keep it as the selected motif and start at stage 2.

## Stage 1: generate and review short motifs

Read [references/motif-generation-and-review.md](references/motif-generation-and-review.md), then use the bundled scripts.

Unless the user asks for different values, generate 12 numbered WAV candidates with the same simple sound and similar duration:

```bash
{python} "{skillDir}/scripts/generate_candidates.py" --output-dir music-workbench/motif-candidates
```

The command must produce and open:

- numbered WAV files;
- `manifest.json`;
- `tracks.js`;
- `review.html`.

If the output directory already contains a batch, the script creates a new timestamped batch directory instead of overwriting it. Use the path printed by the script for the rest of the workflow.

Do not replace the listening page with a text table. Let the user listen and choose by number. Record only the reason they actually give. Copy the chosen WAV to `music-workbench/selected-motif/` without deleting the candidates.

## Stage 2: turn needs into scene prompts

Ask only what is needed to understand:

- what each scene should feel like;
- how energetic or restrained it should be;
- sounds the user wants or dislikes.

If the user does not know instrument names or production terms, draft sensible choices in plain language and let them correct the draft.

Create a short scene list first. After the user confirms the directions, read [references/prompt-template.md](references/prompt-template.md) and produce one prompt per scene. Keep the selected motif as the common melodic source.

Visible result for this stage:

- a confirmed scene list;
- one copyable prompt per scene;
- the selected motif WAV that every scene will use.

Save the confirmed scene list and prompts to `music-workbench/scene-prompts.md`.

## Stage 3: generate with Suno Cover and refine

Read [references/suno-cover.md](references/suno-cover.md) before operating Suno.

Use Suno Cover by default. If the user explicitly chooses another service, preserve the same method with that service's reference-audio arrangement feature.

For the first pass:

1. Upload the selected motif WAV.
2. Choose Cover and an available model suitable for iteration.
3. Keep the track instrumental unless the user asks for vocals.
4. Paste one confirmed scene prompt and generate.
5. Verify that a playable result exists, then save its file or link.

Use an already logged-in browser session when browser automation is available. If browser operation is unavailable, give the user the exact manual steps and wait for the generated result. Never claim that a file was uploaded or a track was generated without verifying it.

Before revising, classify the main problem:

1. The motif disappears or an unrelated theme takes over.
2. The mood or harmony is wrong.
3. The instruments or sound design dominate the piece.
4. The rhythm, bass, or density becomes tiring.
5. The structure or duration does not work as background music.

Change one group of controls per round when possible. Use the failure table in [references/prompt-template.md](references/prompt-template.md). Keep earlier generations.

When the task has more than a few outputs, record each round with [references/iteration-log-template.md](references/iteration-log-template.md).

## Completion checks

Do not call the workflow complete until these exist:

- candidate WAV files and an opened listening page;
- one user-selected motif WAV;
- a confirmed scene list and copyable prompts;
- at least one verified Suno Cover result;
- for any revision, the earlier result, the changed prompt, and the new result.

## Deliverables

```text
music-workbench/
  motif-candidates/
    candidate-01.wav        # first batch when the directory is empty
    ...
    review.html
    tracks.js
    manifest.json
    batch-YYYYMMDD-HHMMSS/  # later batches are preserved here
  selected-motif/
  scene-prompts.md
  scene-versions/
  prompts-and-results.md
```

Use WAV for the reference motif. Make MP3 or M4A copies only when they make review or sharing easier.
