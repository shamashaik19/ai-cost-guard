fetch("http://localhost:8000/status")
  .then(res => res.json())
  .then(data => {
    let html = `<div class='card'>`;

    for (let s in data.services) {
      html += `<p>${s}: ${data.services[s]} | $${data.costs[s]}</p>`;
    }

    html += `<h3>Total: $${data.estimated_monthly_cost}</h3></div>`;
    document.getElementById("data").innerHTML = html;
  });
