<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-grey border border-grey-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Login</h1>
                <p class="mb-6 text-white-500">
                    I am Happy.I am Happy.I am Happy.I am Happy.I am Happy.I am Happy.</br>
                    I am Happy.I am Happy.I am Happy.I am Happy.I am Happy.I am Happy.
                </p>
                <p class="font-bold">
                    Already have an account? <RouterLink to="/login" href="#" class="underline">Click Here</RouterLink> to login!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-red-200 rounded-lg">
                <form class="space-y-6 ">
                    <div>
                        <label>Name</label><br>
                        <input type="text" placeholder="Your Fullname" class="w-full mt-2 py-3 px-6 border border-grey-200 rounded-lg">
                    </div>

                    <div>
                        <label>E-mail</label><br>
                        <input type="email" placeholder="Your Email address" class="w-full mt-2 py-3 px-6 border border-grey-200 rounded-lg">
                    </div>

                    <div>
                        <label>Password</label><br>
                        <input type="password" placeholder="Your password" class="w-full mt-2 py-3 px-6 border border-grey-200 rounded-lg">
                    </div>

                    <div>
                        <label>Repeat Password</label><br>
                        <input type="password" placeholder="Repeat your password" class="w-full mt-2 py-3 px-6 border border-grey-200 rounded-lg">
                    </div>

                    <div>
                        <button class="py-4 px-6 bg-green-600 text-white rounded-lg">Signup</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>