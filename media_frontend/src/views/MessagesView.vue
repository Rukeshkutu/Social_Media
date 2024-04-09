<template>
    <div class="max-w-7xl max-auto grid grid-cols-4 gap-4">

        <!-- --------------Left Column ------------------ -->
        <div class="main-left col-span-1">
            <div class="p-2 bg-white border border-grey-200 rounded-lg">
                <div class="space-y-4">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <img src="../assets/photo.jpeg" class="w-6 rounded-full">
                            <p class="text-xs"><strong>Dipesh Shrestha</strong></p>
                        </div>
                        <span class="text-xs text-grey-500">12 minutes ago</span>
                    </div>

                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <img src="../assets/photo.jpeg" class="w-6 rounded-full">
                            <p class="text-xs"><strong>Dipesh Shrestha</strong></p>
                        </div>
                        <span class="text-xs text-grey-500">12 minutes ago</span>
                    </div>

                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <img src="../assets/photo.jpeg" class="w-6 rounded-full">
                            <p class="text-xs"><strong>Dipesh Shrestha</strong></p>
                        </div>
                        <span class="text-xs text-grey-500">12 minutes ago</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- ---------- Left Column -------------------- -->
        <div class="main-centre col-span-3 space-y-4">
            <div class="bg-white border border-grey-200 rounded-lg">
                <div class="flex flex-col flex-grow p-2">
                    <div class="flex flex-w-full mt-2 space-x-2 max-w-md ml-auto justify-end">
                        <div>
                            <div class="bg-blue-500 text-white p-2 rounded-l-lg rounded-br-lg">
                                <p class="text-sm">my chat my chat my chat my chat my chat my chat my chat my chat my chat my chat my chat</p>
                            </div>
                            <spam class="text-xs text-grey-500 leading-none">2 min ago</spam>
                        </div>
                        
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-grey-300">
                            <img src="../assets/photo.jpeg" class="w-7 h-7 rounded-full">
                        </div>
                    </div>

                    <div class="flex flex-w-full mt-2 space-x-2 max-w-md ml-auto justify-end">
                        <div>
                            <div class="bg-blue-500 text-white p-2 rounded-l-lg rounded-br-lg">
                                <p class="text-sm">Hello Hello Hello Hello Hello </p>
                            </div>
                            <spam class="text-xs text-grey-500 leading-none">2 min ago</spam>
                        </div>
                        
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-grey-300">
                            <img src="../assets/photo.jpeg" class="w-7 h-7 rounded-full">
                        </div>
                    </div>

                    <div class="flex w-full mt-2 space-x-2 max-w-md">
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-grey-300">
                            <img src="../assets/photo.jpeg" class="w-7 h-7 rounded-full">
                        </div>
                        <div>
                            <div class="bg-green-300 p-2 rounded-r-lg rounded-bl-lg">
                                <p class="text-sm">Hello Hello Hello Hello Hello </p>
                            </div>
                            <spam class="text-xs text-grey-500 leading-none">2 min ago</spam>
                        </div>
                    </div>

                    <div class="flex w-full mt-2 space-x-2 max-w-md">
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-grey-300">
                            <img src="../assets/photo.jpeg" class="w-7 h-7 rounded-full">
                        </div>
                        <div>
                            <div class="bg-green-300 p-2 rounded-r-lg rounded-bl-lg">
                                <p class="text-sm">welcome welcome welcome welcome welcome welcome welcome welcome welcome welcome welcome welcome welcome welcome  </p>
                            </div>
                            <spam class="text-xs text-grey-500 leading-none">2 min ago</spam>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-white border border-grey-100 rounded-lg"> 
                <div class="p-1">
                    <textarea class="p-1 w-full bg-yellow-50 rounded-lg border border-grey-200" placeholder="What are you want to say?"></textarea>
                </div>

                <div class="p-1  flex justify-between">
                    <a href="#" class="inline-block py-4 px-6 bg-green-600 text-white rounded-lg">Post</a>
                </div>
            </div>
        </div>
    </div>
</template>