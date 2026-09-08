# Quality standard

Every published task must satisfy the following checks.

1. **Exact execution:** the Python solver reproduces every provided output cell-for-cell.
2. **Readable rule:** the transformation is explained without relying on the code alone.
3. **Provenance:** the source of the rule and implementation is recorded.
4. **Disclosure:** the record states whether the provided test output informed the rule or a repair.
5. **Failure evidence:** ambiguities and failed alternatives are retained when they help distinguish rules.
6. **Determinism:** verification produces the same result in a clean environment.
7. **Schema validity:** grids, colors, dimensions, and task metadata pass automated checks.

## Evidence labels

- `rule_generalized`: a compact rule generates the output from the input.
- `task_specific`: executable and explainable, with assumptions tied to this task.
- `test_repaired`: the provided test output was used to revise or select the implementation.
- `lookup_only`: exact reproduction depends on matching a known input.
- `ambiguous`: multiple rules remain consistent with all provided examples.

All labels may be included in the research corpus. The public interface will expose them so readers can distinguish exact reproduction from evidence of generalization.

