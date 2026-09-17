# Prompt template

Use this reference after a motif has been selected and the user is ready to create scene arrangements.

## Scene card

Fill this out before writing the platform prompt:

```text
Scene label: [scene name or role]
Role in play: [exploration / tension / rest / transition / other]
Energy and pulse: [tempo or plain-language speed]
Main instruments: [...]
Percussion: [...]
Bass: [...]
Space and mix: [dry / close / wide / reverberant / sparse / dense]
Motif treatment: [repeat / octave shift / stretch / shorten / fragments]
Avoid: [...]
Loop or duration needs: [...]
```

Mood words are useful as a summary, but they are not enough on their own. Translate them into sounds the model can act on.

## Arrangement prompt

```text
Instrumental game soundtrack for [scene role], around [tempo or pulse].

[Main instruments and register]. [Percussion behavior]. [Bass behavior].
[Density, room, and mix character].

Use the uploaded motif as the melodic source. Keep its identifying rhythm and pitch shape recognizable. Develop it through repetition, octave changes, timing changes, and short fragments. Create contrast through instrumentation, harmony, rhythm, and texture.

Avoid unrelated themes, extended solos, and free melodic improvisation. Avoid [scene-specific exclusions].
```

Use "only melodic source" when identity needs to be strict. Use "main melodic source" when the tool needs more freedom. Make that change deliberately and record it.

## What to change when a result fails

| What the user hears | Change in the next round |
|---|---|
| The motif appears only at the start or end | Require it in lead phrases throughout the track; allow repetition, octave changes, and fragments; forbid unrelated themes |
| The music becomes a different song in the middle | Remove requests for a contrasting melody, solo, or free improvisation; move contrast to harmony, rhythm, texture, and instruments |
| The overall character does not match the target | Describe the intended register, harmony, room sound, silence, and instrument choices instead of relying on a mood word |
| One sound overwhelms everything | Reduce or remove it, or limit its volume, frequency, register, and role in the arrangement |
| The track is tiring as background music | Lower density, simplify drums or bass, add reduced sections, and leave room for game audio |
| Every version sounds identical | Keep the motif fixed but change the scene's instruments, pulse, harmony, texture, and register |

Do not change all of these at once unless the user wants a complete restart.
