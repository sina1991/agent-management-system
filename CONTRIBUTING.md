# Contributing

## Workflow

1. Read the relevant architecture document and contract before changing behavior.
2. Keep changes focused and compatible with existing contracts unless a contract change is explicitly intended.
3. Update documentation and examples when behavior changes.
4. Run the validation script and tests.
5. Never commit secrets or private project data.

## Agent contributions

Every Agent type should define:
- role and responsibilities;
- allowed inputs and outputs;
- authority boundaries;
- completion criteria;
- reporting format;
- handoff requirements.

New Agent profiles should reuse shared contracts instead of inventing incompatible message formats.
