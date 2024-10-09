import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { createClient } from '@supabase/supabase-js';
import LandingPage from './pages/LandingPage';
import LoginPage from './pages/LoginPage';
import SearchPage from './pages/SearchPage';
import EditPage from './pages/EditPage';
import Navbar from './components/common/Navbar';
import Footer from './components/common/Footer';
import './App.css';

// Initialize Supabase client
const supabase = createClient(
    import.meta.env.VITE_SUPABASE_URL,
    import.meta.env.VITE_SUPABASE_SERVICE_ROLE_KEY
);

function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<LandingPage supabase={supabase} />} />
                <Route path="/login" element={<LoginPage supabase={supabase} />} />
                <Route path="/search" element={<SearchPage supabase={supabase} />} />
                <Route path="/edit" element={<EditPage supabase={supabase} />} />
            </Routes>
            <Footer />
        </Router>
    );

}

export default App
