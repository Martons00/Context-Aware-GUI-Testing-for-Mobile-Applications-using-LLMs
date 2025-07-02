# Project_LLM_A3

## TO-DO
    - Compilare i json
    - Compilare le tabelle
    - Scrivere i i paragrafi su OverLeaf 
    

## Cose Fatte

| App            | DroidBot base | DroidBot Replay output | DroidBot + LLAMA | DroidBot + LLAMA + Scelta | Humanoid base | Humanoid Replay output | Humanoid + LLAMA |
|----------------|:-------------:|:---------------------:|:----------------:|:-------------------------:|:-------------:|:----------------------:|:----------------:|
| PassAndroid    |      RM       |          GM           |        RM        |           RM              |      MR       |          GM            |       RM         |
| TFA pre-log    |      X        |          X            |        RM        |           X               |      MR       |          GM            |       RM         |
| TFA post-log   |      GM       |          GM           |        RM        |           RM              |      RM       |          X            |       RM         |
| Omni-Notes     |      MR       |          GM           |        RM        |           RM              |      MR       |          GM            |       RM         |


Activity coverage e Valid set text in frazioni 

## PassAndroid

| Metric              | DroidBot base | DroidBot Replay output | DroidBot + LLAMA | DroidBot + LLAMA + Scelta | Humanoid base | Humanoid Replay output | Humanoid + LLAMA |
|---------------------|:-------------:|:---------------------:|:----------------:|:-------------------------:|:-------------:|:----------------------:|:----------------:|
| UTG state           |      110      |          110          |       214        |           77              |      170      |          170           |      119         |
| UTG edge            |      200      |          200          |       2087       |           232             |      360      |          360           |      230         |
| Activity coverage   |      4/15     |          4/15         |       4/15       |           5/15            |      4/15     |          4/15          |      5/15        |
| Valid set text      |      0/66     |          0/66         |       0/31       |           7/182           |      0/224    |          0/224         |      8/289       |

## TFA pre-log

| Metric              | DroidBot base | DroidBot Replay output | DroidBot + LLAMA | DroidBot + LLAMA + Scelta | Humanoid base | Humanoid Replay output | Humanoid + LLAMA |
|---------------------|:-------------:|:---------------------:|:----------------:|:-------------------------:|:-------------:|:----------------------:|:----------------:|
| UTG state           |     356       |          356          |       15         |           --              |      19       |          19            |      8           |
| UTG edge            |     615       |          615          |       25         |           --              |      34       |          34            |      19          |
| Activity coverage   |     3/31      |          3/31         |      2/28        |          -/--             |     2/28      |         2/28           |     2/28         |
| Valid set text      |     0/70      |         12/70         |      0/10        |          -/--             |     0/9       |          0/9           |     2/21         |

## TFA post-log

| Metric              | DroidBot base | DroidBot Replay output | DroidBot + LLAMA | DroidBot + LLAMA + Scelta | Humanoid base | Humanoid Replay output | Humanoid + LLAMA |
|---------------------|:-------------:|:---------------------:|:----------------:|:-------------------------:|:-------------:|:----------------------:|:----------------:|
| UTG state           |      226      |         226           |       30         |           54              |      291      |          291           |      37          |
| UTG edge            |     1112      |         1112          |       58         |           86              |      642      |          642           |      79          |
| Activity coverage   |     3/31      |         3/31          |      2/28        |          2/28             |     2/28      |         2/28           |     2/28         |
| Valid set text      |    48/101     |        39/101         |      8/19        |          37/93            |    102/210    |        30/210          |    27/28         |

## Omni-Notes

| Metric              | DroidBot base | DroidBot Replay output | DroidBot + LLAMA | DroidBot + LLAMA + Scelta | Humanoid base | Humanoid Replay output | Humanoid + LLAMA |
|---------------------|:-------------:|:---------------------:|:----------------:|:-------------------------:|:-------------:|:----------------------:|:----------------:|
| UTG states           |      73       |          73           |       296         |           18              |      169       |          169            |      52          |
| UTG edges            |      173       |          173           |       787         |           32              |      419       |          419            |      125          |
| Activity coverage   |      3/15       |          3/15           |       2/15         |           1/15              |      5/15       |          5/15            |      3/15          |
| Valid set text      |      80.65% (50/62)       |          38.71% (24/62)           |       80.65% (25/31)         |           36.47% (31/85)              |      52.91% (91/172)       |          58.14% (100/172)           |       46.84% (74/158)          |

Note: the 'Humanoid base' folder is hidden because it exceeds 100 MB and is included in the .gitignore file.

## Limitazioni

Elenco dei motivi per cui si potrebbero migliorare i risultati:
    - HW e Risorse
    - Più tempo di test
    - Codice del app poco descrittivo nei componenti, poichè il contesto è derivato da quello, se poco esplicativi, il modello ha poche info per essere più accurato.
    - Più app. 
