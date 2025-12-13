// components/SearchBar.jsx
import React from 'react';
import './SearchBar.css';

const SearchBar = ({
  searchTerm,
  setSearchTerm,
  selectedCategory,
  setSelectedCategory,
  priceRange,
  setPriceRange,
  sortOption,
  setSortOption,
  categories,
  sortOptions,
}) => {
  return (
    <div className="search-bar-container">
      <input
        type="text"
        placeholder="Search products..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />

      <select
        value={selectedCategory}
        onChange={(e) => setSelectedCategory(e.target.value)}
      >
        <option value="">All Categories</option>
        {categories.map((cat) => (
          <option key={cat} value={cat}>
            {cat}
          </option>
        ))}
      </select>

      <select
        value={priceRange}
        onChange={(e) => setPriceRange(e.target.value)}
      >
        <option value="">All Prices</option>
        <option value="0-5000">Under ₹5,000</option>
        <option value="5000-20000">₹5,000 - ₹20,000</option>
        <option value="20000-50000">₹20,000 - ₹50,000</option>
        <option value="50000-100000">₹50,000 - ₹1,00,000</option>
      </select>

      <select
        value={sortOption}
        onChange={(e) => setSortOption(e.target.value)}
      >
        <option value="">Sort By</option>
        {sortOptions.map((sort) => (
          <option key={sort} value={sort}>
            {sort}
          </option>
        ))}
      </select>
    </div>
  );
};

export default SearchBar;
