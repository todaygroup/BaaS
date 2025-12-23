import Link from "next/link";

export default function Home() {
    return (
        <div className="flex flex-col items-center justify-center space-y-8 py-12">
            <div className="text-center space-y-4">
                <h2 className="text-4xl font-extrabold tracking-tight sm:text-6xl">
                    저자의 지식을 책으로 만드는 <br />
                    <span className="text-indigo-600">AI 에이전트 인프라</span>
                </h2>
                <p className="text-xl text-slate-600 max-w-2xl mx-auto">
                    BAAS는 한 사람의 저자가 수년간 쌓아온 지식과 스타일을 AI 에이전트 팀에 이식하여, 책 한 권 전체를 고품질로 자동 집필합니다.
                </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-5xl">
                <div className="p-6 bg-white border rounded-xl shadow-sm hover:shadow-md transition-shadow">
                    <h3 className="font-bold text-lg mb-2">기획 및 설계</h3>
                    <p className="text-slate-500 text-sm">에이전트가 책의 아웃라인을 잡고 구조화합니다.</p>
                </div>
                <div className="p-6 bg-white border rounded-xl shadow-sm hover:shadow-md transition-shadow">
                    <h3 className="font-bold text-lg mb-2">리서치 및 집필</h3>
                    <p className="text-slate-500 text-sm">RAG를 통해 저자의 지식을 검색하고 초안을 작성합니다.</p>
                </div>
                <div className="p-6 bg-white border rounded-xl shadow-sm hover:shadow-md transition-shadow">
                    <h3 className="font-bold text-lg mb-2">자기비판 및 수정</h3>
                    <p className="text-slate-500 text-sm">에이전트 비평을 통해 품질을 출판 수준으로 끌어올립니다.</p>
                </div>
            </div>

            <Link
                href="/dashboard"
                className="px-8 py-4 bg-indigo-600 text-white rounded-full font-bold text-lg hover:bg-indigo-700 transition-colors"
            >
                프로젝트 시작하기
            </Link>
        </div>
    );
}
