import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";

const API_BASE = "http://localhost:8050";
const SAMPLE = `Jane Citizen\njane.citizen@example.com\nAcme Corp\n+1 (416) 555-0100\nToronto, ON`;

function App() {
  const [rawText, setRawText] = useState(SAMPLE);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [templates, setTemplates] = useState([]);
  const [providers, setProviders] = useState([]);
  const [templateId, setTemplateId] = useState("contact_intake");
  const [providerId, setProviderId] = useState("heuristic");
  const [minConfidence, setMinConfidence] = useState(0.7);

  useEffect(() => {
    Promise.all([
      fetch(`${API_BASE}/api/templates`).then((r) => r.json()),
      fetch(`${API_BASE}/api/providers`).then((r) => r.json())
    ])
      .then(([templatePayload, providerPayload]) => {
        setTemplates(templatePayload.items);
        setProviders(providerPayload.items);
      })
      .catch(() => {
        setError("Failed loading templates/providers");
      });
  }, []);

  async function submit(event) {
    event.preventDefault();
    setError("");

    try {
      const response = await fetch(`${API_BASE}/api/autofill`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          raw_text: rawText,
          template_id: templateId,
          provider_id: providerId,
          min_confidence: Number(minConfidence)
        })
      });
      if (!response.ok) {
        throw new Error(`Request failed: ${response.status}`);
      }
      setResult(await response.json());
    } catch (e) {
      setError(String(e));
    }
  }

  return (
    <main style={{ maxWidth: 900, margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h1>AI-Assisted Form Autofill</h1>
      <form onSubmit={submit}>
        <div>
          <label>
            Template
            <select value={templateId} onChange={(e) => setTemplateId(e.target.value)} style={{ marginLeft: 8 }}>
              {templates.map((item) => (
                <option key={item.id} value={item.id}>
                  {item.label}
                </option>
              ))}
            </select>
          </label>
          <label style={{ marginLeft: 12 }}>
            Provider
            <select value={providerId} onChange={(e) => setProviderId(e.target.value)} style={{ marginLeft: 8 }}>
              {providers.map((item) => (
                <option key={item.id} value={item.id}>
                  {item.label}
                </option>
              ))}
            </select>
          </label>
        </div>

        <div style={{ marginTop: 10 }}>
          <label>
            Min Confidence: {minConfidence}
            <input
              type="range"
              min="0.5"
              max="0.95"
              step="0.05"
              value={minConfidence}
              onChange={(e) => setMinConfidence(e.target.value)}
              style={{ marginLeft: 8 }}
            />
          </label>
        </div>

        <textarea
          rows={10}
          style={{ width: "100%", marginTop: 12 }}
          value={rawText}
          onChange={(e) => setRawText(e.target.value)}
        />
        <button type="submit" style={{ marginTop: 8 }}>Suggest Fields</button>
      </form>

      {result ? (
        <section style={{ marginTop: 16 }}>
          <h2>Autofill Result</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </section>
      ) : null}
      {error ? <p style={{ color: "crimson" }}>{error}</p> : null}
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
