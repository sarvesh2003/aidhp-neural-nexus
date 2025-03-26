import React, { useEffect, useState } from 'react';
import './Recommendations.css';
import axios from 'axios';

const Recommendations = () => {
    const [recommendations, setRecommendations] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchRecommendations = async () => {
            try {
                const response = await axios.get('http://localhost:5000/api/recommendations');
                setRecommendations(response.data);
            } catch (err) {
                console.error('Error fetching recommendations:', err);
                setError('Failed to load recommendations. Please try again later.');
            } finally {
                setLoading(false);
            }
        };

        fetchRecommendations();
    }, []);

    if (loading) {
        return (
            <div className="container recommendations-page">
                <div className="loading-spinner"></div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="container recommendations-page">
                <div className="error-message">{error}</div>
            </div>
        );
    }

    return (
        <div className="container recommendations-page">
            <h1 className="section-title">Personalized Recommendations</h1>
            <div className="recommendations-grid">
                {recommendations.length > 0 ? (
                    recommendations.map((rec, index) => (
                        <RecommendationCard 
                            key={index}
                            product={rec.product}
                            description={rec.description}
                            index={index}
                        />
                    ))
                ) : (
                    <div className="empty-state">
                        No recommendations available at the moment.
                    </div>
                )}
            </div>
        </div>
    );
};

const RecommendationCard = ({ product, description, index }) => {
    const colors = [
        'linear-gradient(135deg, #ff4e50, #f9d423)',
        'linear-gradient(135deg, #ff416c, #ff4b2b)',
        'linear-gradient(135deg, #ff5f6d, #ffc371)',
        'linear-gradient(135deg, #ff4b1f, #ff9068)'
    ];
    
    return (
        <div 
            className="recommendation-card"
            style={{ background: colors[index % colors.length] }}
        >
            <div className="card-content">
                <h3 className="product-title">{product}</h3>
                <p className="product-desc">{description}</p>
            </div>
            <div className="card-actions">
                <button className="action-btn">Learn More</button>
            </div>
        </div>
    );
};

export default Recommendations;