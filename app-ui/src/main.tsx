import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import './index.css';
import videoBackground from './../public/1025466644-preview_1707954514003.mp4';

const MyComponent = () => {
  return (
    <React.StrictMode>
      <div className='bg-video '>
        <video autoPlay loop muted className='video blur-[5px] brightness-50'>
          <source src={videoBackground} type='video/mp4' />
        </video>
        <div className='content-overlay with-shadow'>
          <App />
        </div>
      </div>
    </React.StrictMode>
  );
};

ReactDOM.createRoot(document.getElementById('root')!).render(<MyComponent />);
