---
name: ai-game-music-workflow
description: Build a recognizable game-music identity from a short motif, then adapt it into consistent scene music with AI. Use when a user needs motif candidates, reference-audio arrangement prompts, cross-scene BGM, or help diagnosing AI music that loses the melody or misses the intended sound.
---

# AI game music workflow

Help the user create a small musical idea that can survive changes in instruments, tempo, rhythm, and scene. The goal is a reusable identity for one game, not one impressive but disconnected track.

Do not imitate the melody or recording of a named game. A reference may explain the desired level of recognizability, but create new musical material.

## Separate preference from diagnosis

- Treat the user's selection as a preference. Record any reason they give without adding musical explanations of your own.
- Explain unfamiliar terms when they first matter. A motif is a short musical idea that can be repeated and changed.
- Use the user's chosen music service when one is named. Otherwise prefer a service that can arrange or extend uploaded audio. Product names, modes, interfaces, and licensing terms change, so verify current details when they affect the task.

## Choose the starting point

If the user already has a short melody or WAV, inspect that material and continue with scene testing.

If the user has no melody, first ask for the broad musical identity: desired tension or warmth, energy, rough tempo, sounds to favor, sounds to avoid, and whether the music will loop under gameplay. Do not require music theory vocabulary.

## Build short motif candidates

Create a small batch of short candidates. Each candidate only needs one phrase that is easy to compare. Choose the batch size and duration according to the project and the user's listening time. Keep the comparison fair:

- use the same simple sound, loudness, and approximate length;
- vary rhythm, rests, pitch movement, register, and repetition;
- number every candidate and preserve earlier batches;
- export separate reviewable audio files and, when useful, a simple comparison page.

The sound only needs to make the notes and rests easy to compare. Do not spend time polishing the arrangement before the motif is chosen.

Let the user select by listening. Useful questions are whether a candidate is memorable, tolerates repetition, can be split into fragments, and fits the game's overall tone. These are prompts for the user's judgment, not facts the agent should assert.

## Test the motif across scenes

Choose a small set of contrasting directions from the game's actual scenes. Validate the method on a few directions before expanding the set. Describe each with concrete controls:

- instruments and register;
- pulse or tempo;
- percussion and bass behavior;
- density, space, and mix character;
- required and forbidden sounds;
- how the motif may change.

Upload the selected motif to a tool that supports reference-audio arrangement or extension. You can first use one scene to check whether the tool preserves the motif before expanding the set. For a reusable prompt structure, read [references/prompt-template.md](references/prompt-template.md).

## Diagnose before changing the prompt

Classify the problem before revising anything:

1. The motif disappears or an unrelated theme takes over.
2. The mood or harmony is wrong.
3. The instruments or sound design dominate the piece.
4. The rhythm, bass, or overall density becomes tiring.
5. The structure or duration does not work as background music.

Change one group of controls per round when possible. This makes the result understandable. Preserve the previous output instead of overwriting it.

When the motif gets lost, require recognizable repetitions, octave changes, timing changes, and short fragments of the uploaded motif. Explicitly forbid unrelated themes, long solos, or free melodic improvisation. Do not force the motif to repeat unchanged from beginning to end; the arrangement still needs room to develop.

When the scene feels wrong, replace vague mood words with audible choices. Specify which instruments to remove, how much bass to keep, whether drums are allowed, how much silence is needed, and whether the mix should feel dry or spacious.

## Keep an iteration record

Record the prompt, platform, model or mode, reference file, result file or link, the one change made in that round, what the user actually heard, and the next decision. Use [references/iteration-log-template.md](references/iteration-log-template.md) when the task has more than a few outputs.

## Decide when a version is usable

A scene version is ready for the current stage when:

- the scene's intended sound is present;
- the motif remains recognizable in important passages;
- later passages do not drift into an unrelated theme;
- bass and density are comfortable for repeated gameplay listening;
- the track leaves enough space for game sounds.

Do not claim that a track is objectively good. Report the user's selection and any observable technical checks separately.

## Deliverables

Keep the work easy to revisit:

```text
music-workbench/
  brief.md
  motif-candidates/
  selected-motif/
  scene-versions/
  prompts-and-results.md
  exports/
```

Use WAV for the editable reference when practical. Make MP3 or M4A copies for easy review.
