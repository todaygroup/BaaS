"use client";

import { useState } from "react";
import OutlineEntryForm from "@/components/book/OutlineEntryForm";

export default function NewBookPage() {
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<any>(null);

    const handleStartPlanning = async (formData: any) => {
        setLoading(true);
        try {
            // In real deployment, this URL should come from env
            const response = await fetch(`http://localhost:8000/graphs/book/run?book_id=${Math.random().toString(36).substring(7)}&topic=${encodeURIComponent(formData.topic)}&audience=${encodeURIComponent(formData.audience)}&tone=${encodeURIComponent(formData.tone)}`, {
                method: "POST",
            });
            const data = await response.json();
            setResult(data.result);
        } catch (error) {
            console.error("Failed to run book graph", error);
            alert("에이전트 실행 중 오류가 발생했습니다.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="max-w-4xl mx-auto space-y-12 py-8">
            <div className="text-center space-y-4">
                <h1 className="text-3xl font-extrabold text-slate-900 sm:text-4xl">새 책 프로젝트 시작</h1>
                <p className="text-slate-600">책의 컨셉을 입력하면 AI 에이전트가 최적의 아웃라인을 설계합니다.</p>
            </div>

            {!result ? (
                <OutlineEntryForm onSubmit={handleStartPlanning} />
            ) : (
                <div className="bg-white p-8 rounded-2xl shadow-xl border border-slate-100 space-y-6">
                    <div className="flex justify-between items-center border-b pb-4">
                        <h2 className="text-2xl font-bold text-indigo-600">생성된 아웃라인</h2>
                        <button
                            onClick={() => setResult(null)}
                            className="text-sm text-slate-400 hover:text-slate-600"
                        >
                            다시 만들기
                        </button>
                    </div>
                    <div className="prose prose-slate max-w-none">
                        <pre className="whitespace-pre-wrap font-sans text-slate-800 leading-relaxed">
                            {result.outline}
                        </pre>
                    </div>
                    <div className="pt-6">
                        <button className="w-full py-4 bg-emerald-600 text-white rounded-xl font-bold hover:bg-emerald-700 transition-colors">
                            이 구성으로 집필 시작하기
                        </button>
                    </div>
                </div>
            )}

            {loading && (
                <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center z-50">
                    <div className="bg-white p-8 rounded-2xl shadow-2xl flex flex-col items-center space-y-4">
                        <div className="w-12 h-12 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin"></div>
                        <p className="font-bold text-slate-700">에이전트 팀이 책을 기획하고 있습니다...</p>
                        <p className="text-sm text-slate-400">평균 30초 내외가 소요됩니다.</p>
                    </div>
                </div>
            )}
        </div>
    );
}
