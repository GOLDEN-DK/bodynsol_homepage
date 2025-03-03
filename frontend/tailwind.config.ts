import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#3B82F6', // 바디앤솔 브랜드 색상으로 변경 필요
          dark: '#2563EB',
          light: '#93C5FD',
        },
        secondary: {
          DEFAULT: '#10B981', // 바디앤솔 보조 색상으로 변경 필요
          dark: '#059669',
          light: '#6EE7B7',
        },
      },
      fontFamily: {
        sans: ['Pretendard', 'sans-serif'],
        heading: ['Pretendard', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

export default config 