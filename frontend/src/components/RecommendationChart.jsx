import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts'

const COLORS = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#ec4899']

function RecommendationChart({ recommendations }) {
  if (!recommendations || recommendations.length === 0) {
    return null
  }

  const data = recommendations.map((item, index) => ({
    ...item,
    color: COLORS[index % COLORS.length],
  }))

  return (
    <section className="section chart-section" aria-labelledby="chart-heading">
      <h2 id="chart-heading" className="section-title">Top 3 Recommendations</h2>
      <div className="chart-container">
        <ResponsiveContainer width="100%" height={250}>
          <BarChart data={data} layout="vertical" margin={{ top: 10, right: 30, left: 10, bottom: 0 }}>
            <YAxis
              dataKey="elective"
              type="category"
              width={180}
              tick={{ fontSize: 13, fill: '#334155' }}
              axisLine={false}
              tickLine={false}
            />
            <XAxis
              type="number"
              domain={[0, 'dataMax + 20']}
              tick={{ fontSize: 12, fill: '#64748b' }}
              axisLine={{ stroke: '#e2e8f0' }}
              tickLine={{ stroke: '#e2e8f0' }}
            />
            <Tooltip
              formatter={(value) => [value + '%', 'Probability']}
              contentStyle={{
                backgroundColor: '#fff',
                border: '1px solid #e2e8f0',
                borderRadius: '8px',
                boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)',
              }}
            />
            <Bar
              dataKey="probability"
              radius={[0, 4, 4, 0]}
              maxBarSize={40}
            >
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.color} />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
      <ul className="recommendation-list" role="list" aria-label="Top recommendations with probabilities">
        {recommendations.map((item, index) => (
          <li key={item.elective} className="recommendation-list-item">
            <span className="recommendation-rank">{index + 1}.</span>
            <span className="recommendation-name">{item.elective}</span>
            <span className="recommendation-probability">{item.probability}%</span>
          </li>
        ))}
      </ul>
    </section>
  )
}

export default RecommendationChart