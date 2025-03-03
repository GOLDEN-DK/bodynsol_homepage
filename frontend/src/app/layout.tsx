import type { Metadata } from 'next'
import '@/styles/globals.css'

export const metadata: Metadata = {
  title: '바디앤솔 - 필라테스 센터 & 아카데미',
  description: '바디앤솔 센터 및 아카데미의 공식 웹사이트입니다. 필라테스 교육, 통증/교정 운동, 강사 양성과정 등 다양한 프로그램을 제공합니다.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="ko">
      <body>
        {children}
      </body>
    </html>
  )
} 