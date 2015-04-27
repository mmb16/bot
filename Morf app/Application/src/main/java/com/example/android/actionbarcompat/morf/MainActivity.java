/*
 * Copyright (C) 2013 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.android.actionbarcompat.morf;

import android.app.SearchManager;
import android.content.Intent;
import android.os.Bundle;
import android.provider.Settings;
import android.support.v4.app.Fragment;
import android.support.v7.app.ActionBar;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;

import org.json.JSONObject;

/**
 * This sample shows you how to use ActionBarCompat with a customized theme. It utilizes a split
 * action bar when running on a device with a narrow display, and show three tabs.
 *
 * This Activity extends from {@link ActionBarActivity}, which provides all of the function
 * necessary to display a compatible Action Bar on devices running Android v2.1+.
 *
 * The interesting bits of this sample start in the theme files
 * ('res/values/styles.xml' and 'res/values-v14</styles.xml').
 *
 * Many of the drawables used in this sample were generated with the
 * 'Android Action Bar Style Generator': http://jgilfelt.github.io/android-actionbarstylegenerator
 */
public class MainActivity extends ActionBarActivity  {

    //Declaring tabs and fragments
    ActionBar.Tab History, Pending, Profile;
    Fragment historyFragmentTab = new HistoryFragmentTab();
    Fragment pendingFragmentTab = new PendingFragmentTab();
    Fragment profileFragmentTab = new ProfileFragmentTab();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Set the Action Bar to use tabs for navigation
        ActionBar ab = getSupportActionBar();

        ab.setDisplayHomeAsUpEnabled(false);
        ab.setDisplayShowTitleEnabled(false);
        ab.setNavigationMode(ActionBar.NAVIGATION_MODE_TABS);

        //Setting custom tab
        History = ab.newTab().setText("History");
        Pending = ab.newTab().setText("Pending");
        Profile = ab.newTab().setText("Profile");

        //Setting tab listeners
        History.setTabListener(new com.example.android.actionbarcompat.morf.TabListener(historyFragmentTab));
        Pending.setTabListener(new com.example.android.actionbarcompat.morf.TabListener(pendingFragmentTab));
        Profile.setTabListener(new com.example.android.actionbarcompat.morf.TabListener(profileFragmentTab));

        //add tab to action bar
        ab.addTab(History);
        ab.addTab(Pending);
        ab.addTab(Profile);

    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate menu from menu resource (res/menu/main)
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.main, menu);
        return super.onCreateOptionsMenu(menu);

    }

    private void openSearch() {
        startActivity(new Intent(SearchManager.INTENT_ACTION_GLOBAL_SEARCH));
    }
    private void openSettings() {
        startActivity(new Intent(Settings.ACTION_SETTINGS));
    }
    private void signOut() {
        startActivity(new Intent (this, LoginActivity.class));
    }

    private void openSplit() {
        startActivity(new Intent (this, Split.class));
    }
    private void openPay() {
        startActivity(new Intent (this, Pay.class));
    }
    private void openRequest() {
        startActivity(new Intent (this, Request.class));
    }



    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        switch (item.getItemId()) {
            case R.id.action_search:
                openSearch();
                return true;
            case R.id.action_settings:
                openSettings();
                return true;
            case R.id.action_split:
                openSplit();
                return true;
            case R.id.action_request:
                openRequest();
                return true;
            case R.id.action_pay:
                openPay();
                return true;
            case R.id.action_sign_out:
                signOut();
            default:
                return super.onOptionsItemSelected(item);
        }

    }

    /** Called when the user clicks the Send button */
    public void findFriends(View view) {
        // Do something in response to button
        Intent intent = new Intent(this, FindFriends.class);
        startActivity(intent);
    }
    public void cashOut(View view) {
        // Do something in response to button
        Intent intent = new Intent(this, CashOut.class);
        startActivity(intent);
    }
    public void createGroup(View view) {
        // Do something in response to button
        Intent intent = new Intent(this, CreateGroup.class);
        startActivity(intent);
    }
    public void openBanks(View view) {
        // Do something in response to button
        Intent intent = new Intent(this, OpenBanks.class);
        startActivity(intent);
    }


}
