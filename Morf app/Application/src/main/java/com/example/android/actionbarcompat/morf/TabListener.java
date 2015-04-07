package com.example.android.actionbarcompat.morf;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.ActionBar;
import android.support.v7.app.ActionBar.Tab;

/**
 * Created by MohB on 3/19/15.
 */
public class TabListener implements ActionBar.TabListener{

    private Fragment fragment;

    public TabListener(Fragment fragment) {
        this.fragment = fragment;
    }

    @Override
    public void onTabSelected(Tab tab, FragmentTransaction fragmentTransaction) {
        fragmentTransaction.replace(R.id.activity_main, fragment);
        // This is called when a tab is selected.
    }

    // Implemented from ActionBar.TabListener
    @Override
    public void onTabUnselected(Tab tab, FragmentTransaction fragmentTransaction) {
        fragmentTransaction.remove(fragment);
        // This is called when a previously selected tab is unselected.
    }

    // Implemented from ActionBar.TabListener
    @Override
    public void onTabReselected(Tab tab, FragmentTransaction fragmentTransaction) {
        // This is called when a previously selected tab is selected again.
    }
}
