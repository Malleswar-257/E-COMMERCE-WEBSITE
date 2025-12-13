import phone1 from '../assets/Smartphones/phone1.png';
import phone2 from '../assets/Smartphones/phone2.png';
import laptop1 from '../assets/Laptops/laptop1.png';
import laptop2 from '../assets/Laptops/laptop2.png';
import laptop3 from '../assets/Laptops/laptop3.png';
import headphone1 from '../assets/Headphones/headphone1.png';
import headphone2 from '../assets/Headphones/headphone2.png';
import speaker from '../assets/speaker.png';
import smartwatch from '../assets//smartwatch.png';

const allProducts = [
  { id: 1, name: 'iPhone 14', price: 69999, image: phone1, category: 'Smartphones' },
  { id: 2, name: 'Samsung Galaxy S22', price: 64999, image: phone2, category: 'Smartphones' },
  { id: 3, name: 'MacBook Air M2', price: 119999, image: laptop1, category: 'Laptops' },
  { id: 4, name: 'Dell XPS 13', price: 99999, image: laptop2, category: 'Laptops' },
  { id: 5, name: 'HP Pavilion', price: 74999, image: laptop3, category: 'Laptops' },
  { id: 6, name: 'Sony WH-1000XM5', price: 29999, image: headphone1, category: 'Headphones' },
  { id: 7, name: 'JBL Tune 760NC', price: 6999, image: headphone2, category: 'Headphones' },
  { id: 8, name: 'Boat Stone 1200F', price: 3499, image: speaker, category: 'Speakers' },
  { id: 9, name: 'Apple Watch SE', price: 29999, image: smartwatch, category: 'Wearables' },
];

export default allProducts;
