"use client";

import { useState } from "react";

export default function OutlineEntryForm({ onSubmit }: { onSubmit: (data: any) => void }) {
    const [topic, setTopic] = useState("");
    const [audience, setAudience] = useState("");
    const [tone, setTone] = useState("Professional");

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSubmit({ topic, audience, tone });
    };

    return (
        <form onSubmit={handleSubmit} className="space-y-6 max-w-2xl mx-auto p-8 bg-white rounded-2xl shadow-xl border border-slate-100">
            <div className="space-y-2">
                <label className="text-sm font-semibold text-slate-700">책의 주제나 핵심 아이디어</label>
                <textarea
                    required
                    value={topic}
                    onChange={(e) => setTopic(e.target.value)}
                    placeholder="예: AI 에이전트를 활용한 B2B 세일즈 자동화 전략"
                    className="w-full h-32 p-4 rounded-xl border border-slate-200 focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none transition-all resize-none"
                />
            </div>

            <div className="space-y-2">
                <label className="text-sm font-semibold text-slate-700">주요 독자층</label>
                <input
                    type="text"
                    required
                    value={audience}
                    onChange={(e) => setAudience(e.target.value)}
                    placeholder="예: 테크 스타트업 세일즈 팀장 및 경영진"
                    className="w-full p-4 rounded-xl border border-slate-200 focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none transition-all"
                />
            </div>

            <div className="space-y-2">
                <label className="text-sm font-semibold text-slate-700">집필 톤앤매너</label>
                <select
                    value={tone}
                    onChange={(e) => setTone(e.target.value)}
                    className="w-full p-4 rounded-xl border border-slate-200 focus:ring-2 focus:ring-indigo-500 focus:border-transparent outline-none transition-all bg-white"
                >
                    <option value="Professional">전문적이고 신뢰감 있는</option>
                    <option value="Friendly">친근하고 대화체 스타일의</option>
                    <option value="Action-oriented">실무 지향적이고 간결한</option>
                </select>
            </div>

            <button
                type="submit"
                className="w-full py-4 bg-indigo-600 text-white rounded-xl font-bold hover:bg-indigo-700 transform active:scale-[0.98] transition-all shadow-lg hover:shadow-indigo-200"
            >
                아웃라인 생성 시작하기
            </button>
        </form>
    );
}
