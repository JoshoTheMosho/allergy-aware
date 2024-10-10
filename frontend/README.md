# Allergy Management App

## Overview

The Allergy Management App is designed to help users manage and track allergens in various dishes offered by restaurants. The frontend is built using React and MUI for UI/UX.

## Features

- User authentication (login)
- Search for dishes based on allergens or ingredients

## Installation

### Prerequisites

- npm
- [Supabase](https://supabase.io/) account and project

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/allergy-management-app.git
    cd allergy-management-app/frontend
    ```

2. Install the required dependencies:

    ```bash
    npm install
    ```

4. Set up environment variables:

    Create a `.env` file in the root directory and add your Supabase URL and key:

    ```env
    SUPABASE_URL=your_supabase_url
    SUPABASE_KEY=your_supabase_key
    ```

5. Run the React application:

    ```bash
    npm run dev
    ```

    The application will be available at `http://localhost:5173`.

## Project Structure

```plaintext
allergy-aware/
├── frontend/
│   ├── public/
│   │   ├── vite.svg
│   ├── src/
│   │   ├── assets/
│   │   │   ├── react.svg
│   │   ├── components/
│   │   │   ├── common/
│   │   │   │   ├── Footer.jsx
│   │   │   │   ├── Navbar.jsx
│   │   │   ├── editData/
│   │   │   │   ├── EditData.jsx
│   │   │   ├── landing/
│   │   │   │   ├── Landing.jsx
│   │   │   ├── login/
│   │   │   │   ├── Login.jsx
│   │   │   ├── searchIngredients/
│   │   │   │   ├── SearchIngredients.jsx
│   │   ├── pages/
│   │   │   ├── EditPage.jsx
│   │   │   ├── LandingPage.jsx
│   │   │   ├── LoginPage.jsx
│   │   │   ├── SearchPage.jsx
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── main.jsx
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   ├── vite.config.js
├── backend/
│   ├── README.md/
│   ├── ...
├── .gitignore
├── README.md