# Suno Cover workflow

Use this reference for stage 3.

Suno changes its interface and model availability over time. Locate controls by their visible names instead of saved screen coordinates. If the interface no longer matches this guide, verify the current route in Suno's official help before continuing.

Official references:

- Audio uploads: https://help.suno.com/en/articles/6141569
- Cover: https://help.suno.com/en/articles/2872257
- Model selection: https://help.suno.com/en/articles/13924993

## Before uploading

- Use the selected motif WAV from stage 1.
- Confirm that the user owns or is allowed to upload the audio.
- Reuse the user's logged-in browser session. Do not request or handle their password.
- Model access, upload limits, and credit costs can differ by account. Check what the interface shows.

## Browser-assisted route

When browser automation is available:

1. Open Suno Create.
2. Find `Audio`, `Upload Audio`, or `Add Audio`.
3. Choose `Upload` or `My Device`, then select the motif WAV.
4. Accept the ownership confirmation only when the user owns the material.
5. Select `Cover`. Depending on the current interface, it may appear in the Create form or under the uploaded track's `More Actions → Create → Cover`.
6. Select an available model. A faster model is suitable for early iterations; do not assume a particular model is available.
7. Keep the result instrumental and leave lyrics empty unless the user asks for vocals.
8. Paste the confirmed scene prompt into the style or prompt field.
9. Review the selected reference file, mode, model, prompt, and any displayed credit cost.
10. Create the track when the user's request authorizes generation. Do not repeatedly retry a failed generation if it may consume credits.
11. Wait until a playable result appears. Save its link or download it to the scene output folder.

Do not report success merely because the upload dialog closed. Verify the uploaded item, the selected Cover mode, and a playable generated result.

## Manual route

When browser automation is unavailable, give the user these same steps in short form and stop at the point where their action is required. Continue only after they provide the generated file or link.

Never imply that the Skill itself uploaded or generated anything when the user completed the operation manually.

## Refinement loop

After the user listens:

1. Record their words.
2. Choose the single largest problem.
3. Use the failure table in `prompt-template.md`.
4. Change one group of prompt controls.
5. Generate one new round with the same motif WAV.
6. Keep both results and record the difference.

Examples of one-group changes:

- reduce bass and drum density;
- remove an unwanted instrument family;
- make the motif restriction stricter;
- change space from wide and reverberant to dry and close.

Do not change genre, instruments, bass, tempo, density, and structure all at once unless the user explicitly asks for a restart.
