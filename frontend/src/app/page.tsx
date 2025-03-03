export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold text-center mb-8">바디앤솔에 오신 것을 환영합니다</h1>
        <p className="text-center mb-8">
          바디앤솔 센터 및 아카데미의 공식 웹사이트입니다.
        </p>
        <div className="flex justify-center gap-4">
          <button className="bg-primary text-white px-6 py-2 rounded-md">
            센터 이용하기
          </button>
          <button className="bg-secondary text-white px-6 py-2 rounded-md">
            아카데미 교육 살펴보기
          </button>
        </div>
      </div>
    </main>
  )
} 