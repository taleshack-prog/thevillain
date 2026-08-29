/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Scaffold: não bloquear build por lint (mantemos TS checando o código).
  eslint: { ignoreDuringBuilds: true },
};
export default nextConfig;
