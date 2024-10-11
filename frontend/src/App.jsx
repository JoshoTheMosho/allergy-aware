import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import LoginPage from './pages/LoginPage';
import SearchPage from './pages/SearchPage';
import EditPage from './pages/EditPage';
import Navbar from './components/common/Navbar';
import Footer from './components/common/Footer';
import './App.css';

function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/search" element={<SearchPage />} />
                <Route path="/edit" element={<EditPage />} />
            </Routes>
            <Footer />
        </Router>
    );

}

export default App
