document.addEventListener('DOMContentLoaded', function () {
  const themeToggle = document.getElementById('themeToggle');
  const body = document.body;
  const savedTheme = localStorage.getItem('opticrops-theme');

  if (savedTheme === 'dark') {
    body.classList.add('theme-dark');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      body.classList.toggle('theme-dark');
      const isDark = body.classList.contains('theme-dark');
      localStorage.setItem('opticrops-theme', isDark ? 'dark' : 'light');
    });
  }

  const forms = document.querySelectorAll('.needs-validation');
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener('submit', function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  });

  if (typeof modelMetrics !== 'undefined' && typeof cropCounts !== 'undefined') {
    renderDashboardCharts(modelMetrics, cropCounts);
  }
});

function renderDashboardCharts(metrics, cropCounts) {
  const accuracyLabels = Object.keys(metrics).filter((key) => key !== 'selected_model' && key !== 'data_shape');
  const accuracyValues = accuracyLabels.map((label) => Number(metrics[label].accuracy.toFixed(3)));

  const accuracyCanvas = document.getElementById('accuracyChart');
  if (accuracyCanvas) {
    new Chart(accuracyCanvas, {
      type: 'bar',
      data: {
        labels: accuracyLabels,
        datasets: [{
          label: 'Accuracy',
          data: accuracyValues,
          backgroundColor: accuracyLabels.map(() => 'rgba(25, 135, 84, 0.7)'),
          borderColor: accuracyLabels.map(() => 'rgba(25, 135, 84, 1)'),
          borderWidth: 1,
        }],
      },
      options: {
        responsive: true,
        scales: {
          y: { beginAtZero: true, max: 1 },
        },
      },
    });
  }

  const cropCanvas = document.getElementById('cropChart');
  if (cropCanvas) {
    new Chart(cropCanvas, {
      type: 'doughnut',
      data: {
        labels: Object.keys(cropCounts),
        datasets: [{
          data: Object.values(cropCounts),
          backgroundColor: [
            '#198754', '#20c997', '#0dcaf0', '#ffc107', '#fd7e14', '#6610f2', '#d63384', '#6f42c1', '#0d6efd', '#adb5bd',
          ],
        }],
      },
      options: {
        responsive: true,
        plugins: { legend: { position: 'bottom' } },
      },
    });
  }
}
