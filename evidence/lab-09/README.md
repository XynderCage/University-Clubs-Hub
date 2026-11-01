# LAB-09 evidence index

Produced: pattern decisions, framework decision, ADR-002, detailed class model and repository port. Team must verify names after merge and record critique revision.

An alternative editable class diagram and matching SVG for comparison against detailed class model. Addresses these issues:
- The diagram used json_response(), while the implementation uses _json().
- Method parameters, return types and contact fields needed more detail.
- The pattern decisions needed clearer alternatives and accepted costs.


The pattern-decisions document was expanded with alternatives and trade-offs.

Test status:
Executed tests/test_lab09_interfaces.py using Python 3.14.7.
All 3 tests passed:
- Search uses the injected repository and trims surrounding whitespace.
- An overlong query is rejected before reaching the repository.
- Detail retrieval returns the repository result, including None for a missing ID.

These tests verify the service/interface boundary. SQLite filtering and
browser behaviour were not tested in this run.