# LittleLemon Restaurant API

Welcome to the API documentation for the LittleLemon Restaurant project. Here you'll find instructions on how to interact with various endpoints and functionalities.

## Table of Contents
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
  - [Menu Items](#menu-items)
  - [Bookings](#bookings)
- [Testing with Insomnia](#testing-with-insomnia)
- [Error Handling](#error-handling)
- [Dependencies and Setup](#dependencies-and-setup)
- [General Notes](#general-notes)

## Authentication

1. **Obtaining a Token**: 
   - Make a POST request to \`http://127.0.0.1:8000/auth/token/login/\` with \`username\` and \`password\` in the request body. The response will include the authentication token.
2. **Using the Token**: 
   - Include the token as a Bearer token in the Authorization header for endpoints requiring authentication (e.g., table bookings).

## API Endpoints

### Menu Items

- **List and Create Menu Items**: 
  - **GET or POST**: \`http://127.0.0.1:8000/restaurant/menu/\`
  - **POST Example**: \`{"title": "Ice Cream", "price": 80}\`
- **Retrieve, Update, or Delete a Single Menu Item**: 
  - **GET, PUT, DELETE**: \`http://127.0.0.1:8000/restaurant/menu/<int:pk>\`

### Bookings

- **List, Create, Update, and Delete Bookings**: 
  - Accessed through the default router at \`http://127.0.0.1:8000/restaurant/booking/\`
  - Requires authentication.

### Authentication and Authorization (Djoser)

- Various endpoints under \`http://127.0.0.1:8000/auth/\` for user management.

## Testing with Insomnia

- Download and install the Insomnia client from [here](https://insomnia.rest/download).
- Follow the authentication steps above to obtain a token.
- Use Insomnia to send requests to the provided endpoints.

## Error Handling

- Common error codes include 404 (Not Found), 401 (Unauthorized), and 405 (Method Not Allowed).

## Dependencies and Setup

- Dependencies include Django, Django REST Framework, and Djoser.
- Run \`python manage.py makemigrations\` and \`python manage.py migrate\` to apply database migrations.

## General Notes

- Make sure to follow the appropriate request formats for POST and PUT requests.
- Report any issues or feedback to the project maintainers.
