# UI Competitor Benchmark

## Competitors Reviewed

- Formstack Field Prefill: https://www.formstack.com/features/field-prefill
- Typeform branching logic: https://help.typeform.com/hc/en-us/articles/360029116392-What-is-branching-logic
- Typeform URL parameters: https://www.typeform.com/developers/create/url-parameters/
- Fillout conditional logic: https://www.fillout.com/docs/help/conditional-integration
- Jotform feature catalog: https://www.jotform.com/features/

## Key Patterns Observed

- Modern form systems combine prefill + conditional logic + save/review loops.
- Template-driven flows reduce setup friction and standardize outputs.
- Confidence/review thresholds help route ambiguous extractions to humans.

## Implemented Adaptations

- Added template registry and provider abstraction.
- Added configurable minimum confidence threshold for review routing.
- Added missing-required and review-required field outputs.
- Updated frontend with template/provider selectors and confidence tuning controls.
