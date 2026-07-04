document.addEventListener('DOMContentLoaded', function () {

    // Sidebar toggle for mobile
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('emsSidebar');
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function () {
            sidebar.classList.toggle('show');
        });
        document.addEventListener('click', function (event) {
            if (window.innerWidth < 992 &&
                sidebar.classList.contains('show') &&
                !sidebar.contains(event.target) &&
                !sidebarToggle.contains(event.target)) {
                sidebar.classList.remove('show');
            }
        });
    }

    // Auto-dismiss alerts after 5 seconds
    document.querySelectorAll('.alert').forEach(function (alertEl) {
        setTimeout(function () {
            const alertInstance = bootstrap.Alert.getOrCreateInstance(alertEl);
            if (alertInstance) {
                alertInstance.close();
            }
        }, 5000);
    });

    // Show loading spinner on navigation link / form submit clicks
    const spinner = document.getElementById('loadingSpinner');
    if (spinner) {
        document.querySelectorAll('a.ems-nav-loading, .ems-sidebar .nav-link').forEach(function (link) {
            link.addEventListener('click', function () {
                spinner.classList.remove('d-none');
            });
        });
        window.addEventListener('beforeunload', function () {
            spinner.classList.remove('d-none');
        });
    }

    // Confirmation prompt for any delete link that opts in via data-confirm
    document.querySelectorAll('[data-confirm]').forEach(function (el) {
        el.addEventListener('click', function (event) {
            if (!confirm(el.getAttribute('data-confirm'))) {
                event.preventDefault();
            }
        });
    });
});
