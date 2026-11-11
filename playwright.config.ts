import {defineConfig,devices} from "@playwright/test";
export default defineConfig({testDir:"./tests",fullyParallel:false,workers:2,webServer:{command:"npm run dev",url:"http://localhost:3000",reuseExistingServer:false},use:{baseURL:"http://localhost:3000",trace:"retain-on-failure"},projects:[{name:"desktop",use:{...devices["Desktop Chrome"]}},{name:"mobile",use:{...devices["iPhone 13"],browserName:"chromium"}}]});

