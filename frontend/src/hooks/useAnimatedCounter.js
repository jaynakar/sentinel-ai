import { useEffect, useState } from "react";

export default function useAnimatedCounter(endValue, duration = 1500) {
  const [count, setCount] = useState(0);

  useEffect(() => {
    if (typeof endValue !== "number") {
        setCount(0);
        return;
    }

    let start = 0;
    const startTime = performance.now();

    const animate = (currentTime) => {
      const progress = Math.min(
        (currentTime - startTime) / duration,
        1
      );

      const currentValue = start + (endValue - start) * progress;

      setCount(currentValue);

      if (progress < 1) {
        requestAnimationFrame(animate);
      }
    };

    requestAnimationFrame(animate);

  }, [endValue, duration]);

  return count;
}