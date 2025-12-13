import React, { useEffect, useState } from 'react';
import '../styles/Hero.css';

const ads = [
  '/ads/ad1.png',
  '/ads/ad2.png',
  '/ads/ad3.png'
];

const Hero = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isAutoScroll, setIsAutoScroll] = useState(true);

  useEffect(() => {
    let interval = null;
    if (isAutoScroll) {
      interval = setInterval(() => {
        setCurrentIndex((prev) => (prev + 1) % ads.length);
      }, 5000);
    }
    return () => clearInterval(interval);
  }, [isAutoScroll, currentIndex]);

  const goToPrev = () => {
    setIsAutoScroll(false);
    setCurrentIndex((prev) => (prev - 1 + ads.length) % ads.length);
  };

  const goToNext = () => {
    setIsAutoScroll(false);
    setCurrentIndex((prev) => (prev + 1) % ads.length);
  };

  const goToSlide = (index) => {
    setIsAutoScroll(false);
    setCurrentIndex(index);
  };

  return (
    <div className="hero-wrapper">
      {ads.map((image, index) => (
        <img
          key={index}
          src={image}
          alt={`Slide ${index}`}
          className={`slide ${index === currentIndex ? 'active' : ''}`}
        />
      ))}

      {/* Navigation Buttons */}
      <div className="nav-button left" onClick={goToPrev}>
        ❮
      </div>
      <div className="nav-button right" onClick={goToNext}>
        ❯
      </div>

      {/* Dots */}
      <div className="dot-navigation">
        {ads.map((_, index) => (
          <span
            key={index}
            className={`dot ${index === currentIndex ? 'active' : ''}`}
            onClick={() => goToSlide(index)}
          />
        ))}
      </div>
    </div>
  );
};

export default Hero;
