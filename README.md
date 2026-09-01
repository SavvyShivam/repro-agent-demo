# repro-agent-demo

A tiny Flask API used as a fixture for the [Solari Issue Repro Agent](https://github.com/solari-sdk/solari-cookbook/tree/main/examples/issue-repro-agent-py).

It ships with one deliberate bug — see the open issue. `GET /widgets?limit=0`
returns all five widgets instead of an empty list, because the handler guards
with `if limit:` and `0` is falsy.

```bash
pip install -r requirements.txt
python -m pytest -q        # the two existing tests pass; none cover limit=0
python app.py             # then: curl 'http://localhost:5000/widgets?limit=0'
```
