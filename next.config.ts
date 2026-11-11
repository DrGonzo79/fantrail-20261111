import type {NextConfig} from "next";
const repo="fantrail-20261111";
const isPages=process.env.PAGES_BUILD==="true";
const config:NextConfig={output:"export",trailingSlash:true,basePath:isPages?`/${repo}`:"",assetPrefix:isPages?`/${repo}/`:undefined,images:{unoptimized:true}};
export default config;
