import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
    title: "BAAS - Book-Authoring Agent System",
    description: "AI-powered book authoring infrastructure",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="ko">
            <body className={inter.className}>
                <div className="min-h-screen bg-slate-50 text-slate-900">
                    <header className="border-b bg-white px-6 py-4">
                        <h1 className="text-xl font-bold text-indigo-600">BAAS</h1>
                    </header>
                    <main className="container mx-auto p-6">{children}</main>
                </div>
            </body>
        </html>
    );
}
