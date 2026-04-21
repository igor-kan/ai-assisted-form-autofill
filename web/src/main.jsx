import React, { useState } from "react";
import { createRoot } from "react-dom/client";

const SAMPLE = `Jane Citizen\njane.citizen@example.com\n+1 (416) 555-0100\nToronto, ON`;

function App() {
  const [rawText, setRawText] = useState(SAMPLE);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function submit(event) {
    event.preventDefault();
    setError("");

    try {
      const response = await fetch("http://localhost:8050/api/autofill", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ raw_text: rawText })
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
    <main style={{ maxWidth: 820, margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h1>AI-Assisted Form Autofill</h1>
      <form onSubmit={submit}>
        <textarea
          rows={10}
          style={{ width: "100%" }}
          value={rawText}
          onChange={(e) => setRawText(e.target.value)}
        />
        <button type="submit" style={{ marginTop: 8 }}>Suggest Fields</button>
      </form>

      {result ? <pre>{JSON.stringify(result, null, 2)}</pre> : null}
      {error ? <p style={{ color: "crimson" }}>{error}</p> : null}
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
