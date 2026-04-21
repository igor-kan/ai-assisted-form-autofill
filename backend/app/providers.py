from .extract import extract_fields


class HeuristicProvider:
    id = "heuristic"
    label = "Heuristic Extractor"

    def run(self, raw_text: str) -> dict:
        return extract_fields(raw_text)


class MockLlmProvider:
    id = "mock_llm"
    label = "Mock LLM Provider"

    def run(self, raw_text: str) -> dict:
        # Deterministic wrapper to simulate an alternate provider path.
        fields = extract_fields(raw_text)
        for value in fields.values():
            value["confidence"] = min(1.0, value["confidence"] + 0.03)
        return fields


PROVIDERS = {
    HeuristicProvider.id: HeuristicProvider(),
    MockLlmProvider.id: MockLlmProvider(),
}


def list_providers() -> list[dict]:
    return [{"id": key, "label": provider.label} for key, provider in PROVIDERS.items()]


def resolve_provider(provider_id: str):
    return PROVIDERS.get(provider_id, PROVIDERS["heuristic"])
