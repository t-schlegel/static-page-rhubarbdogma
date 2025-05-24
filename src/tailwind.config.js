/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./pages/**/*.py", "./components/**/*.py"],
  theme: {
    extend: {
      fontFamily: {
        times: ['"Times New Roman"', "Times", "serif"],
      },
      scale: {
        102: "1.02",
      },
      gridTemplateColumns: {
        100: "repeat(100, minmax(0, 1fr))",
      },
      gridTemplateRows: {
        100: "repeat(100, minmax(0, 1fr))",
      },
      gridColumn: {
        "span-13": "span 13 / span 13",
        "span-14": "span 14 / span 14",
        "span-15": "span 15 / span 15",
        "span-16": "span 16 / span 16",
        "span-18": "span 18 / span 18",
        "span-20": "span 20 / span 20",
        "span-22": "span 22 / span 22",
        "span-25": "span 25 / span 25",
        "span-26": "span 26 / span 26",
        "span-28": "span 28 / span 28",
        "span-30": "span 30 / span 30",
        "span-40": "span 40 / span 40",
        // ... add more if needed
        "span-100": "span 100 / span 100",
      },
      gridColumnStart: {
        ...Array.from({ length: 100 }, (_, i) => ({
          [i + 1]: `${i + 1}`,
        })).reduce((acc, curr) => ({ ...acc, ...curr }), {}),
      },
      gridColumnEnd: {
        ...Array.from({ length: 100 }, (_, i) => ({
          [i + 1]: `${i + 1}`,
        })).reduce((acc, curr) => ({ ...acc, ...curr }), {}),
      },
      gridRow: {
        "span-13": "span 13 / span 13",
        "span-14": "span 14 / span 14",
        "span-15": "span 15 / span 15",
        "span-16": "span 16 / span 16",
        "span-18": "span 18 / span 18",
        "span-20": "span 20 / span 20",
        "span-22": "span 22 / span 22",
        "span-25": "span 25 / span 25",
        "span-26": "span 26 / span 26",
        "span-28": "span 28 / span 28",
        "span-30": "span 30 / span 30",
        "span-40": "span 40 / span 40",
        // ... add more if needed
        "span-100": "span 100 / span 100",
      },
      gridRowStart: {
        ...Array.from({ length: 100 }, (_, i) => ({
          [i + 1]: `${i + 1}`,
        })).reduce((acc, curr) => ({ ...acc, ...curr }), {}),
      },
      gridRowEnd: {
        ...Array.from({ length: 100 }, (_, i) => ({
          [i + 1]: `${i + 1}`,
        })).reduce((acc, curr) => ({ ...acc, ...curr }), {}),
      },
    },
  },
};
