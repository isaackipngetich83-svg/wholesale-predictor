const form = document.getElementById('predict-form');
const resultCard = document.getElementById('result-card');
const predictionValue = document.getElementById('prediction-value');

if (form) {
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    resultCard.hidden = true;

    const formData = new FormData(form);
    const payload = {};
    for (const [key, value] of formData.entries()) {
      payload[key] = value;
    }

    try {
      const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        const error = await response.json().catch(() => ({}));
        throw new Error(error.error || 'Prediction request failed');
      }

      const data = await response.json();
      predictionValue.textContent = Number(data.prediction).toFixed(2);
      resultCard.hidden = false;
    } catch (error) {
      alert(error.message);
    }
  });
}
