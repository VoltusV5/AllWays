export function getCSRFToken() {
    const csrfToken = document.cookie.match(/csrftoken=([\w-]+)/);
    console.log("Extracted CSRF token from cookies:", csrfToken ? csrfToken[1] : 'NOT FOUND');
    return csrfToken ? csrfToken[1] : '';
}
