import React, { useEffect, useState } from 'react';
import Chart from './components/Chart';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
  const [candles, setCandles] = useState([]);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);

  const userId = new URLSearchParams(window.location.search).get('user_id') || 'demo';

  useEffect(() => {
    fetch(`${API_URL}/game/start?user_id=${userId}`)
      .then(res => res.json())
      .then(data => {
        setCandles(data.candles);
        setLoading(false);
      });
  }, []);

  const handleGuess = (direction) => {
    fetch(`${API_URL}/game/submit`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId, prediction: direction })
    })
      .then(res => res.json())
      .then(data => setResult(data));
  };

  if (loading) return <p>Загрузка...</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>GraphRace</h2>
      <Chart candles={candles} />
      <div style={{ marginTop: 20 }}>
        <button onClick={() => handleGuess('up')}>📈 Вверх</button>
        <button onClick={() => handleGuess('down')}>📉 Вниз</button>
      </div>
      {result && (
        <p>
          {result.result ? '✅ Правильно!' : '❌ Неверно!'} <br />
          Направление было: {result.correct_direction === 'up' ? 'Вверх' : 'Вниз'}
        </p>
      )}
    </div>
  );
}

export default App;
