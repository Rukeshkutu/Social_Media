<template>
    <div class="max-w-7xl mz-auto grid grid-cols-4 gap-4">

         <!-- -------- Left Column -->

        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-grey-200 text-center round-lg">
                <img src="../assets/photo.jpeg" class="mb-3 rounded-full">
                <p><strong>Dipesh Shrestha</strong></p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-grey-500"> 23 friends</p>
                    <p class="text-xs text-grey-500"> 244 posts</p>
                </div>

            </div>
        </div>

        <!--  ---------- Center Column ----------------- -->
         
        <div class="main-center col-span-2 space-y-4">
            <div class="bg-white border border-grey-100 rounded-lg"> 
                <div class="p-1">
                    <textarea class="p-1 w-full bg-yellow-50 rounded-lg border border-grey-200" placeholder="What are you thinking?"></textarea>
                </div>

                <div class="p-1  flex justify-between">
                    <a href="#" class="inline-block py-3 px-3 bg-green-600 text-white text-xs rounded-lg">Attach Image</a>

                    <a href="#" class="inline-block py-3 px-9 bg-green-600 text-white text-xs rounded-lg">Post</a>
                </div>
            </div>
            <!-- ------- Post ---------- -->
            <div class="p-4 bg-white border border-grey-200 rounded-lg">
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="../assets/photo.jpeg" class="w-[20px] rounded-full">
                        <p class="text-xs"><strong>Dipesh Shrestha</strong></p>
                    </div>
                    <p class="text-grey-600 text-xs">18 minutes ago</p>
                </div>
                <img src="../assets/flower.jpeg" class="w-full rounded-lg">
                <div class="my-6 flex justify-between">
                    <div class="flex space-x-6">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                            </svg>
                            <span class="text-grey-600 text-xs">23 likes</span>
                        </div>
                    </div>
                    
                    <div class="flex justify-between">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.625 9.75a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 0 1 .778-.332 48.294 48.294 0 0 0 5.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z" />
                            </svg>
                            <span class="text-grey-500 text-xs">0 comment</span>
                        </div>
                    </div>

                    <div class="flex justify-between">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                                <path fill-rule="evenodd" d="M15.75 4.5a3 3 0 1 1 .825 2.066l-8.421 4.679a3.002 3.002 0 0 1 0 1.51l8.421 4.679a3 3 0 1 1-.729 1.31l-8.421-4.678a3 3 0 1 1 0-4.132l8.421-4.679a3 3 0 0 1-.096-.755Z" clip-rule="evenodd" />
                            </svg>
                            <span class="text-grey-500 text-xs"> 0 shares</span>
                        </div>
                    </div>

                    <div>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" />
                        </svg>
                    </div>
                </div>

 
            </div>

            <div class="p-4 bg-white border border-grey-200 rounded-lg">
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="../assets/photo.jpeg" class="w-[20px] rounded-full">
                        <p class="text-xs"><strong>Dipesh Shrestha</strong></p>
                    </div>
                    <p class="text-grey-600 text-xs">18 minutes ago</p>
                </div>
                <p>This is my first post.This is my first post.This is my first post.This is my first post.This is my first post.</p>
                <div class="my-6 flex justify-between">
                    <div class="flex space-x-6">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                            </svg>
                            <span class="text-grey-600 text-xs">23 likes</span>
                        </div>
                    </div>
                    
                    <div class="flex justify-between">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M8.625 9.75a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 0 1 .778-.332 48.294 48.294 0 0 0 5.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z" />
                            </svg>
                            <span class="text-grey-500 text-xs">0 comment</span>
                        </div>
                    </div>

                    <div class="flex justify-between">
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6">
                                <path fill-rule="evenodd" d="M15.75 4.5a3 3 0 1 1 .825 2.066l-8.421 4.679a3.002 3.002 0 0 1 0 1.51l8.421 4.679a3 3 0 1 1-.729 1.31l-8.421-4.678a3 3 0 1 1 0-4.132l8.421-4.679a3 3 0 0 1-.096-.755Z" clip-rule="evenodd" />
                            </svg>
                            <span class="text-grey-500 text-xs"> 0 shares</span>
                        </div>
                    </div>

                    <div>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" />
                        </svg>
                    </div>
                </div>
            </div>
        </div>

        <!-- ------------ Right Column ----------- -->

        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />
            <!-- ----------- Trends --------------- -->
            <Trends />
        </div>
    </div>
</template>

<style scoped>
.inline-block{
    width: 100px;
    height: 40px;
}
</style>
<script>
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
export default{
    name: 'FeedView',
    components:{
        PeopleYouMayKnow,
        Trends,
    }
}
</script>