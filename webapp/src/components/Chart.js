import React from 'react';

function Chart({ candles }) {
  const height = 200;
  const width = 300;
  const padding = 10;
  const max = Math.max(...candles.map(c => c.HIGH));
  const min = Math.min(...candles.map(c => c.LOW));
  const scaleY = val => height - ((val - min) / (max - min)) * (height - padding * 2);

  return (
    <svg width={width} height={height} style={{ background: '#111', margin: '10px 0' }}>
      {candles.map((c, i) => {
        const x = i * 10 + padding;
        const yOpen = scaleY(c.OPEN);
        const yClose = scaleY(c.CLOSE);
        const yHigh = scaleY(c.HIGH);
        const yLow = scaleY(c.LOW);
        const color = c.CLOSE >= c.OPEN ? '#4caf50' : '#f44336';
        return (
          <g key={i}>
            <line x1={x + 5} x2={x + 5} y1={yHigh} y2={yLow} stroke={color} />
            <rect x={x} y={Math.min(yOpen, yClose)} width={10} height={Math.abs(yClose - yOpen)} fill={color} />
          </g>
        );
      })}
    </svg>
  );
}

export default Chart;
