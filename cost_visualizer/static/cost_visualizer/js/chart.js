document.getElementById('cost-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const accountCount = document.querySelector('input[name="account_count"]').value;
    fetch('/calculate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: `account_count=${accountCount}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }
        // Render chart
        const ctx = document.getElementById('chart').getContext('2d');
        // Destroy existing chart if any to prevent overlap
        if (window.myChart) {
            window.myChart.destroy();
        }
        window.myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Regular Accounts', 'Compressed Accounts'],
                datasets: [{
                    label: 'Cost (USD)',
                    data: [data.regular_cost, data.compressed_cost],
                    backgroundColor: ['#ff6384', '#36a2eb']
                }]
            },
            options: {
                scales: {
                    y: { beginAtZero: true, title: { display: true, text: 'Cost (USD)' } }
                },
                plugins: {
                    title: { display: true, text: `Cost for ${accountCount} Accounts` }
                }
            }
        });
        // Update history table dynamically
        fetch('/')
            .then(response => response.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const newTable = doc.querySelector('table');
                document.querySelector('table').outerHTML = newTable.outerHTML;
            });
    });
});