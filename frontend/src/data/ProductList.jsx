// pages/ProductList.jsx
import React, { useState } from 'react';
import ProductCard from '../components/ProductCard';
import allProducts from './product';
import SearchBar from '../components/SearchBar';
import './ProductList.css';

const categories = ['Smartphones', 'Laptops', 'Headphones', 'Speakers', 'Wearables'];
const sortOptions = ['Price: Low to High', 'Price: High to Low'];

const ProductList = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [priceRange, setPriceRange] = useState('');
  const [sortOption, setSortOption] = useState('');

  const filterProducts = () => {
    let filtered = [...allProducts];

    if (searchTerm) {
      filtered = filtered.filter((p) =>
        p.name.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    if (selectedCategory) {
      filtered = filtered.filter((p) => p.category === selectedCategory);
    }

    if (priceRange) {
      const [min, max] = priceRange.split('-').map(Number);
      filtered = filtered.filter((p) => p.price >= min && p.price <= max);
    }

    if (sortOption === 'Price: Low to High') {
      filtered.sort((a, b) => a.price - b.price);
    } else if (sortOption === 'Price: High to Low') {
      filtered.sort((a, b) => b.price - a.price);
    }

    return filtered;
  };

  return (
    <div className="product-list-container">
      <SearchBar
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        selectedCategory={selectedCategory}
        setSelectedCategory={setSelectedCategory}
        priceRange={priceRange}
        setPriceRange={setPriceRange}
        sortOption={sortOption}
        setSortOption={setSortOption}
        categories={categories}
        sortOptions={sortOptions}
      />
      <div className="product-list">
        {filterProducts().map((p) => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  );
};

export default ProductList;
