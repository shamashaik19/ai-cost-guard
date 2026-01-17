const API_URL = "http://localhost:8000/status";

const container = document.getElementById("data");

container.innerHTML = `<p class="loading">Loading AWS services...</p>`;

fetch(API_URL)
  .then((res) => {
    if (!res.ok) {
      throw new Error("Failed to fetch data");
    }
    return res.json();
  })
  .then((data) => {
    let html = `<div class="dashboard">`;

    for (let service in data.services) {
      html += `
        <div class="service-card">
          <h3>${service}</h3>
          <p class="status">Instances: ${data.services[service]}</p>
          <p class="cost">$${data.costs[service]}</p>
        </div>
      `;
    }

    html += `
      <div class="total-card">
        <h2>Total Estimated Monthly Cost</h2>
        <h1>$${data.estimated_monthly_cost}</h1>
      </div>
    </div>`;

    container.innerHTML = html;
  })
  .catch((err) => {
    container.innerHTML = `
      <p class="error">
         Unable to load AWS data.<br/>
        Check backend or AWS credentials.
      </p>
    `;
    console.error(err);
  });
