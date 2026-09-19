function LoadingSpinner({ size = 24 }) {
  return (
    <span
      className="spinner"
      style={{ width: size, height: size }}
      aria-hidden="true"
    />
  )
}

export default LoadingSpinner