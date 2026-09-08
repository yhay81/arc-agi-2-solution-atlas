# Third-party components

## re-arc DSL

`src/arc_agi_2_atlas/re_arc_dsl.py` and solution modules marked with the `re-arc`
concept are derived from the
[re-arc project](https://github.com/michaelhodel/re-arc). They are distributed under
the MIT License; see `LICENSES/re-arc-MIT.txt`.

Every imported program is re-run against all corresponding ARC-AGI-2 provided
training and test pairs in this repository.

## arc-agi2-solutions

`src/arc_agi_2_atlas/providers/our_task_solutions.py`,
`src/arc_agi_2_atlas/providers/llm_task_solutions.py`, and solution modules marked
with the `arc-agi2-solutions` concept are derived from
[ArunSehrawat/arc-agi2-solutions](https://github.com/ArunSehrawat/arc-agi2-solutions).
They are distributed under the MIT License; see
`LICENSES/arc-agi2-solutions-MIT.txt`.

## arc-abstractions

Solution modules marked with the `arc-abstractions` concept are derived from the
[arc-abstractions project](https://github.com/thebowenfeng/arc-abstractions).
They are distributed under the MIT License; see
`LICENSES/arc-abstractions-MIT.txt`.

Only programs that match every corresponding ARC-AGI-2 training and test pair
are included.

## ARC-AGI-2 task data

Files under `data/training` and `data/evaluation` follow the official
[ARC-AGI-2 dataset](https://github.com/arcprize/ARC-AGI-2). They are distributed
under the Apache License 2.0; see `LICENSES/ARC-AGI-2-Apache-2.0.txt`.
